import pandas as pd

from customer_processor import CustomerProcessor


def find_private_investigator() -> pd.DataFrame:

    processor = CustomerProcessor("noahs-csv/noahs-customers.csv")
    processor.add_last_name_column()
    processor.df["phone-num-no-gaps"] = processor.df["phone"].str.replace("-", "")

    def convert_string_to_phone_number(string) -> str:
        letter_to_number = {
            "a": "2",
            "b": "2",
            "c": "2",
            "d": "3",
            "e": "3",
            "f": "3",
            "g": "4",
            "h": "4",
            "i": "4",
            "j": "5",
            "k": "5",
            "l": "5",
            "m": "6",
            "n": "6",
            "o": "6",
            "p": "7",
            "q": "7",
            "r": "7",
            "s": "7",
            "t": "8",
            "u": "8",
            "v": "8",
            "w": "9",
            "x": "9",
            "y": "9",
            "z": "9",
        }

        phone_number = ""
        for letter in string.lower():
            # check if the letter is in the dictionary, and append the corresponding number
            if letter in letter_to_number:
                phone_number += letter_to_number[letter]
            else:
                phone_number += letter
        return phone_number

    processor.df["name-into-number"] = processor.df["lastname"].apply(
        convert_string_to_phone_number
    )

    result = processor.df[
        (processor.df["name-into-number"] == processor.df["phone-num-no-gaps"])
    ]

    return result


if __name__ == "__main__":
    find_private_investigator()
