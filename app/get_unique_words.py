def get_unique_words(text: str) -> List[str]:
    unique_words = text.lower().split()
    return list(set(unique_words))
