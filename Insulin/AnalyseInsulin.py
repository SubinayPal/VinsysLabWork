import re
with open("./Insulin/preproinsulin-seq.txt") as file:
    original_text = file.read()
    print(original_text)
    
cleaned_text = re.sub(r"[A-Z0-9/\s]", "", original_text)

print(len(cleaned_text))

# take 24 char from cleaned_text and put that into a new file after creating the file

first_24_amino_acids = cleaned_text[:24]

with open("lsinsulin-seq-clean.txt", "w") as output_file:
    output_file.write(first_24_amino_acids)

print("Length of saved text:", len(first_24_amino_acids))


# take chars from cleaned_text and put that into a new file after creating the file
amino_acids_25_54 = cleaned_text[24:54]  


with open("./Insulin/binsulin-seq-clean.txt", "w") as output_file:
    output_file.write(amino_acids_25_54)


print("Length of saved text:", len(amino_acids_25_54))


# chars 55–89
amino_acids_55_89 = cleaned_text[54:89]  # indices 54 to 88 (inclusive)

with open("./Insulin/cinsulin-seq-clean.txt", "w") as output_file:
    output_file.write(amino_acids_55_89)

print("Length of saved text:", len(amino_acids_55_89))

# chars from 90 to 110
amino_acids_90_110 = cleaned_text[89:110]

with open("ainsulin-seq-clean.txt", "w") as output_file:
    output_file.write(amino_acids_90_110)
    
print("Length of saved text:", len(amino_acids_90_110))