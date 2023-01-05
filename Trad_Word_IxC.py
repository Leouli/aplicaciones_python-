import os
import sys
import win32com.client
import googletrans
import tkinter as tk

def get_text_from_word_document(filename):
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(filename)
    doc_text = doc.Content.Text
    doc.Close()
    word.Quit()
    return doc_text

def translate_text(text, src_lang, dest_lang):
    translator = googletrans.Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

def show_translation(translated_text):
    window = tk.Tk()
    window.title("Translation")
    window.geometry("400x200")
    label = tk.Label(window, text=translated_text)
    label.pack()
    window.mainloop()

def main():
    filename = r"C:\Users\lenovo\Documents\Cv\filename.docx"
    src_lang = "en"
    dest_lang = "es"
    text = get_text_from_word_document(filename)
    translated_text = translate_text(text, src_lang, dest_lang)
    show_translation(translated_text)

if __name__ == "__main__":
    main()
