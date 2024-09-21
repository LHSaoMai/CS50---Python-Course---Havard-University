from fpdf import FPDF


def main():
    congrat_name = input("Name : ")

    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    # Set the title font
    pdf.set_font("helvetica","", 25)

    # Set the position for the title
    pdf.set_xy(10, 10)  # Adjust the position as needed

    # Add the title
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")

    # Add an image
    page_width = pdf.w
    page_margin = 10
    usable_width = page_width - 2 * page_margin  # Account for margins
    image_width = 200
    # Calculate the x position to center the image
    x_position = (usable_width - image_width) / 2 + page_margin

    # Add an image centered
    pdf.image("shirtificate.png", x=x_position, y=40, w=image_width)

    ##### Now the text #####

    # Set the font for the middle text
    pdf.set_font("helvetica", "", 25)
    pdf.set_text_color(255, 255, 255)


    # Set the position for the middle text
    pdf.set_xy(18,85)  # Adjust x position as needed

    # Add the middle text
    middle_text = f"{congrat_name} took CS50"
    pdf.cell(0, 24, middle_text,align="C")


    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()
