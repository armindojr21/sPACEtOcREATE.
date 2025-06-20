from fpdf import FPDF

#iNSERTING tHE tITLE
class PDF(FPDF):
    def header(self):
        self.set_fill_color(245, 245, 245)
        self.rect(0, 0, 210, 297, 'F')
        #logo
        self.image('house.png', 10, 8, 35)
        #font
        self.set_font('helvetica', 'UB', 24)
        #padding
        self.cell(80)
        # text
        self.set_fill_color(155, 155, 155)
        self.set_text_color(100, 100, 100)
        self.cell(61, 15, "Flatmates' Bill", border=1, ln=1, align='C', fill=True)
        #lINEbREAKER
        self.ln(20)




#iNSERTING tABLE
pdf = PDF()
pdf.add_page()
pdf.set_font(family='times',size=16, style='B')
line_height = pdf.font_size * 3.5


pdf.cell(40, 40, ln=1)
pdf.cell(1)

pdf.cell(63, line_height, 'Va', border=1, align='C')
pdf.cell(63, line_height, 'daysmmmmmmmmmmm', border=1, align='C')
pdf.cell(63, line_height, 'bill', border=1, ln=1, align='C')
pdf.set_font(family='times',size=16)
pdf.cell(1)
pdf.cell(63, line_height, 'Va', border=1, align='C')
pdf.cell(63, line_height, 'days', border=1, align='C')
pdf.cell(63, line_height, 'bill', border=1, ln=1, align='C')
pdf.cell(1)
pdf.cell(63, line_height, 'Ar', border=1, align='C')
pdf.cell(63, line_height, 'days', border=1, align='C')
pdf.cell(63, line_height, 'bill', border=1, ln=1, align='C')
pdf.set_font(family='times',size=16, style='B')
pdf.cell(1)
pdf.cell(189, line_height, "Bill's Period: March, 2024.", border=1, ln=1, align='C')

pdf.output("electric_bill.pdf", 'F')