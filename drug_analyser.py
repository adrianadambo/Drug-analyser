import csv
import sys, time, random
from art import *
#import pyttsx3
#engine = pyttsx3.init()

def main():
    query = input(
        "Hi! This is the Therapeutic Drug Database Decoder. What drug would you like to know about? "
    )
    drug = query.title()
    new_match = "new_match.csv"
    drug_index = get_index(new_match, drug)

    new_target = "finaltarget.csv"
    target_index = get_target(new_target, drug_index)

    filename = "targetindication.csv"
    indications_list = get_indication(target_index, filename)
    if indications_list:
        new_list = [line.replace(",", " ") for line in indications_list]
        final_list = [replace_first_space(text) for text in new_list]
        print(f"The applications of {drug} are: ")
        for code in final_list:
            if code.startswith("Approved"):
                new_code = code.replace(" ", " for ", 1)
                slow_type(new_code)
            else:
                slow_type(code)

    answer = input(
        f"Would you like to know how {drug} works? Please enter 'yes' or 'no': "
    )
    if answer == "yes":
        file = "target4.csv"
        function = get_function(target_index, file)
        if function:
            function_text = function.replace(",", " ")
            slow_type(f"Sure! {drug} physiology is:\n{function_text}")
        else:
            print("We couldn't find the function")
    inst = input(
        f"Would you like to know other names for {drug}? Please enter 'yes' or 'no': "
    )
    if inst == "yes":
        new_file = "synonyms.csv"
        synonyms = get_synonym(drug_index, new_file)
        if synonyms:
            print(f"{drug} is also called: ", *synonyms, sep="\n")
        else:
            print("Unavailable")
    final = input("Is that all? ")
    slower_type(
        f"Thats all I can do for you. I hope you found what you needed about {drug}."
    )
    tprint("Bye!", font="block", chr_ignore=True)

def replace_first_space(line):
    if line.startswith("approved"):
        first_space = line.find(" ")
        if first_space != -1:
            new_line = (
                line[:first_space] + " for" + line[first_space + 1 :]
            )
            return new_line
    else:
        return line


def add_for(final_list):
    for code in final_list:
        if code.startswith("Approved"):
            modified_code = code.replace(" ", " for", 1)
            return modified_code
        else:
            return code

def slower_type(text):
    typing_speed = 70
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print("")

def slow_type(text):
    typing_speed = 200
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print("")


def drugs_to_csv(input_file, output_file):
    with open(input_file) as txt_file, open(
        output_file, "w", newline=""
    ) as csv_file:
        new_csv = csv.writer(csv_file, delimiter=",")

        header = ["index", "title", "drug"]
        new_csv.writerow(header)
        for line in txt_file:
            line = line.strip()
            data = line.split()
            new_csv.writerow(data)


def get_index(new_match, drug):
    with open(new_match, "r") as file:
        csv_reader = csv.DictReader(file)
        found=False
        for row in csv_reader:
            if row["drug"] == drug:
                return row["index"]
                found=True
                break


        if not found:
            sys.exit(f"{drug} not found in the CSV. Try typing the scientific name of the drug.")


def get_target(new_target, drug_index):
    with open(new_target, "r") as file:
        csv_reader = csv.DictReader(file)
        found = False
        for row in csv_reader:
            if row["drug"] == drug_index:
                return row["index"]
                found = True
                break

        if not found:
            print(f"Sorry we couldn't find the target index of this drug")


def get_function(target_index, file):
    with open(file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["index"] == target_index:
                if row["title"] == "FUNCTION":
                    return row["drug"]
        return None


def new_csv(input_filename, output_filename):
    with open(input_filename, "r") as input_file, open(
        output_filename, "w", newline=""
    ) as output_file:
        out_writer = csv.writer(output_file)

        for line in input_file:
            rows = line.strip().split(",", 2)
            if len(rows) >= 3:
                index = rows[0]
                title = rows[1]
                drug = rows[2]

                out_writer.writerow([index, title, drug])


def get_indication(target_index, filename):
    with open(filename, "r") as file:
        new_reader = csv.DictReader(file)
        next(new_reader)
        indications = []
        for row in new_reader:
            if row["index"] == target_index and row["title"] == "INDICATI":
                indications.append(row["indication"])
        return indications


def get_synonym(drug_index, new_file):
    with open(new_file, "r") as file:
        new_reader = csv.DictReader(file)
        next(new_reader)
        synonyms = []
        for row in new_reader:
            if row["index"] == drug_index and row["title"] == "SYNONYMS":
                synonyms.append(row["synonym"])
        return synonyms if len(synonyms) >= 1 else None


if __name__ == "__main__":
    main()
