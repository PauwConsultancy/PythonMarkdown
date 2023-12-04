from markdown import Markdown

def main():
    md = Markdown()

    md.addTitle("Markdown Title", Markdown.TitleLevel.H1)
    md.addParagraph("This is a sample paragraph in Markdown.")

    md.startBlockQuote()
    md.addMarkdown("This is inside a block quote.")
    md.endBlockQuote()

    md.addOrderedList(["First item", "Second item", "Third item"])
    md.addUnorderedList(["Bullet one", "Bullet two", "Bullet three"])

    md.addLink("Pauw Consultancy", "https://www.pauwconsultancy.nl/")
    md.addImage("Sample Image", "https://example.com/image.png")

    sample_code = "print('Hello, World!')"
    md.addCode(sample_code, language="python")

    md.addHorizontalRule()

    md.addTable(["Header1", "Header2"], [["Row1 Col1", "Row1 Col2"], ["Row2 Col1", "Row2 Col2"]])

    md.addBoldText("Bold Text")
    md.addItalicText("Italic Text")
    md.addStrikethroughText("Strikethrough Text")
    md.addInlineCode("Inline code")

    md.addNewLine(2)
    md.addMarkdown("End of Markdown Document")

    print(str(md))

if __name__ == "__main__":
    main()
