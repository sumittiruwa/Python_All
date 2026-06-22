class CV:
    def __init__(self, name, phone, email, address, skills, education, experience):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.skills = skills
        self.education = education
        self.experience = experience

    def display(self):
        print("\n================ CV ================\n")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Address:", self.address)

        print("\nSkills:")
        for s in self.skills:
            print("-", s)

        print("\nEducation:")
        for e in self.education:
            print("-", e)

        print("\nExperience:")
        for ex in self.experience:
            print("-", ex)

        print("\n===================================\n")

    def save(self, filename="cv.txt"):
        with open(filename, "w") as f:
            f.write("========= CV =========\n")
            f.write(f"Name: {self.name}\n")
            f.write(f"Phone: {self.phone}\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Address: {self.address}\n\n")

            f.write("Skills:\n")
            for s in self.skills:
                f.write(f"- {s}\n")

            f.write("\nEducation:\n")
            for e in self.education:
                f.write(f"- {e}\n")

            f.write("\nExperience:\n")
            for ex in self.experience:
                f.write(f"- {ex}\n")

            f.write("\n====================\n")

        print("CV saved successfully as cv.txt")