import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    # User prompt
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    # API call
    for _ in range(20):
        function_results = []
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config = types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
        )
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)


        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")


                function_call_result = call_function(function_call)
                if not function_call_result.parts:
                    raise Exception("Function call failed: .parts empty")
                if not function_call_result.parts[0].function_response:
                    raise Exception("Function call failed: No FunctionResponse object")
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("Function call failed: .response empty")
                function_results.append(function_call_result.parts[0])
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(types.Content(role="user", parts=function_results))
        else:
            print(response.text)
            break
        if _ == 19:
            print("Maximum number of iterations reached")
            exit(1)

if __name__ == "__main__":
    main()
