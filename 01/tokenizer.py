import tiktoken

def main():
    print("Tokens zählen")
    user_input = input("Gib deinen Text ein: ")
    get_tokens(user_input)

def get_tokens(user_input):
# eine für das Modell passende Encoding laden
    encoding = tiktoken.get_encoding("cl100k_base")

# Jetzt können wir einen Text in eine Liste von Tokens verwandeln
    token_integers = encoding.encode(user_input)

#  Anzahl ermitteln 
    tokens_usage = len(token_integers)

    tokenized_input = list(
        map(
            lambda x: encoding.decode_single_token_bytes(x).decode("utf-8"),
            token_integers,
        )
    )
    print(f"Encoding: {encoding}")
    print(f"Token-Integer: {token_integers}")
    print(f"Anzahl an Tokens: {tokens_usage}")
    print(f"Einzelne Tokens: {tokenized_input}")

if __name__ == "__main__":
    main()
