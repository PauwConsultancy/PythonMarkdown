from enum import Enum

class Markdown:

    class TitleLevel(Enum):
        H1 = 1
        H2 = 2
        H3 = 3
        H4 = 4
        H5 = 5
        H6 = 6

    def __init__(self):
        self.md = ""
        self.blockQuoteLevel = 0

    def startBlockQuote(self):
        self.blockQuoteLevel += 1

    def endBlockQuote(self):
        if self.blockQuoteLevel > 0:
            self.blockQuoteLevel -= 1

    def addMarkdown(self, text, noNewlines = 0):
        suffix = '\n' * noNewlines
        if self.blockQuoteLevel > 0:            
            prefix = '> ' * self.blockQuoteLevel
            quoted_text = '\n'.join([f"{prefix}{line}" for line in text.split('\n')])
            self.md += quoted_text + suffix
        else:
            self.md += text + suffix

    def addTitle(self, title, level=TitleLevel.H1):
        if isinstance(level, Markdown.TitleLevel):
            level = level.value
        self.addMarkdown( f"{'#' * level} {title}" , 2)

    def addParagraph(self, paragraph):
        self.addMarkdown( f"{paragraph}", 2)

    def addOrderedList(self, items):        
        for i, item in enumerate(items, 1):
            self.addMarkdown( f"{i}. {item}", 1 )

    def addUnorderedListItem(self, item):
        self.addMarkdown( f"- {item}", 1 )

    def addUnorderedList(self, items):
        for item in items:
            self.addUnorderedListItem(item)

    def addLink(self, text, url):
        self.addMarkdown( f"[{text}]({url})", 2 )

    def addImage(self, alt_text, url):
        self.addMarkdown( f"![{alt_text}]({url})", 2 )

    def addCode(self, code, language=""):
        self.addMarkdown( f"```{language}\n{code}\n```", 2 )


    def addHorizontalRule(self):
        self.addMarkdown( "---", 2 )

    def addTable(self, headers, rows):
        header_row = "| " + " | ".join(headers) + " |"
        separator = "| " + " | ".join(["---"] * len(headers)) + " |"
        self.addMarkdown( header_row, 1 )
        self.addMarkdown( separator, 1 )
        for row in rows:
            self.addMarkdown( "| " + " | ".join(row) + " |", 1 )
        self.addNewLine()

    def addBoldText(self, text):
        self.addMarkdown( f"**{text}** " )

    def addItalicText(self, text):
        self.addMarkdown( f"*{text}* " )

    def addStrikethroughText(self, text):
        self.addMarkdown( f"~~{text}~~ " )

    def addInlineCode(self, code):
        self.addMarkdown( f"`{code}` " )

    def addNewLine(self, count=1):
        self.addMarkdown( "", count )

    def __str__(self):
        return self.md.strip()  
