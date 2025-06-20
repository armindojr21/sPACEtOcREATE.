from fpdf import FPDF
from datetime import datetime


class Bill:
    """
    Creates an object which contains the amount of the
    bill, and the period of the same bill.
    """
    def __init__(self, amount, period):
        self.amount = amount

        self.period = period

class Flatmate:
    """
    Stores the information of a person who lives
    in a flat and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name

        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        p = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        v = round(bill.amount *  p, 2)
        return v

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
    # iNSERTING tHE tITLE
        class PDF(FPDF):
            def header(self):
                self.set_fill_color(245, 245, 245)
                self.rect(0, 0, 210, 297, 'F')
                # logo
                self.image('house.png', 10, 8, 35)
                # font
                self.set_font('helvetica', 'UB', 24)
                # padding
                self.cell(80)
                # text
                self.set_fill_color(155, 155, 155)
                self.set_text_color(100, 100, 100)
                self.cell(61, 15, "Flatmates' Bill", border=1, ln=1, align='C', fill=True)
                # lINEbREAKER
                self.ln(20)

        # iNSERTING tABLE
        pdf = PDF()
        pdf.add_page()
        pdf.set_font(family='times', size=16, style='B')
        line_height = pdf.font_size * 3.5

        pdf.cell(40, 40, ln=1)
        pdf.cell(1)

        pdf.cell(63, line_height, 'Resident', border=1, align='C')
        pdf.cell(63, line_height, 'Days In House', border=1, align='C')
        pdf.cell(63, line_height, 'Part Of Bill', border=1, ln=1, align='C')
        pdf.set_font(family='times', size=16)
        pdf.cell(1)
        pdf.cell(63, line_height, flatmate1.name, border=1, align='C')
        pdf.cell(63, line_height, str(flatmate1.days_in_house), border=1, align='C')
        pdf.cell(63, line_height, f'US${str(flatmate1.pays(bill=bill, flatmate2=flatmate2))}', border=1, ln=1, align='C')
        pdf.cell(1)
        pdf.cell(63, line_height, flatmate2.name, border=1, align='C')
        pdf.cell(63, line_height, str(flatmate2.days_in_house), border=1, align='C')
        pdf.cell(63, line_height, f'US${str(flatmate2.pays(bill=bill, flatmate2=flatmate1))}', border=1, ln=1, align='C')
        pdf.set_font(family='times', size=16, style='B')
        pdf.cell(1)
        pdf.cell(189, line_height, f"Bill's Period: {bill.period}.", border=1, ln=1, align='C')

        pdf.cell(40, 20, ln=1)

        pdf.set_font(family='times', size=16)
        pdf.cell(1)
        pdf.cell(189, line_height, f'Total bill is US${str(bill.amount)} ', border=0, ln=1, align='C')

        pdf.cell(2, 30, ln=1)
        pdf.cell(1)

        agora = datetime.now()
        agora_sem_micsec = agora.strftime('%Y-%m-%d %H:%M:%S')

        pdf.set_font(family='times', size=16, style='U')
        pdf.cell(189, line_height, f'Matola, {agora_sem_micsec}', align='R')
        pdf.output(self.filename, 'F')
        


the_bill = Bill(amount=float(input('What is the has the amount of the electricity bill? US$')),
period=str(input('What was the period of the bill? e.g.[March 2022] ').capitalize()))

n = str(input('Who is the first flatmate? '))
f1 = Flatmate(name=n, days_in_house=int(input(f'How many days has {n} spent in the house? ')))
n = str(input('Who is the other flatmate? '))
f2 = Flatmate(name=n, days_in_house=int(input(f'How many days has {n} spent in the house? ')))

print(f'{f1.name} will pay the amount of US${f1.pays(bill=the_bill, flatmate2=f2)}!')
print(f'{f2.name} will pay the amount of US${f2.pays(bill=the_bill, flatmate2=f1)}!')

pdf_file = PdfReport(filename='report_bill.pdf')

pdf_file.generate(flatmate1=f1, flatmate2=f2, bill=the_bill)





