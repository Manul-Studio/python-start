#ćwiczenie  5.14.5
text = 'X-DSPAM-Confidence: 0.8475'
pierwszy = text.find(':')
print(pierwszy)
drugi = text[pierwszy+1:]
print(float(drugi))
