import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog, ttk

def process_audio_files(directory, task_choice, language_name, report_type_var, model_var, output_directory, acceptable_extensions):
    global root  # Declare root as a global variable
    # Change to the directory where the script is executed
    os.chdir(directory)
    for root, dirs, files in os.walk(directory):
        for audio_file in files:
            if any(audio_file.endswith(ext) for ext in acceptable_extensions):
                audio_path = os.path.join(root, audio_file)
                output_filename_srt = os.path.splitext(audio_file)[0] + '.srt'
                output_filename_txt = os.path.splitext(audio_file)[0] + '.txt'
                output_filename_json = os.path.splitext(audio_file)[0] + '.json'
                output_filename_tsv = os.path.splitext(audio_file)[0] + '.tsv'
                output_filename_vtt = os.path.splitext(audio_file)[0] + '.vtt'
                
                output_path_srt = os.path.join(output_directory, output_filename_srt)
                output_path_txt = os.path.join(output_directory, output_filename_txt)
                output_path_json = os.path.join(output_directory, output_filename_json)
                output_path_tsv = os.path.join(output_directory, output_filename_tsv)
                output_path_vtt = os.path.join(output_directory, output_filename_vtt)

                cmd = [
    'whisper',
    audio_path,
    '--task', task_choice,
    '--language', language_name,
    '--output_format', report_type_var,  # Generate all files
    '--model', model_var, #Choose Model (Small, Medium or large)
    '--fp16', 'False',  # Adding fp16=False option
    '--output_dir', output_directory  # Adding the output directory flag
]

                try:
                    subprocess.run(cmd)
                    # Manually move the output to the desired directory
                    #shutil.move(output_filename_srt, output_path_srt)
                    #shutil.move(output_filename_txt, output_path_txt)
                    #shutil.move(output_filename_, output_path_json)
                    #shutil.move(output_filename_tsv, output_path_tsv)
                    #shutil.move(output_filename_vtt, output_path_vtt)
                    print(f"Processed {audio_path}")
                except Exception as e:
                    print(f"An error occurred while processing {audio_path}: {e}")
    print("All audio files have been processed.")
    exit() #close the thinter window

def main():
    root = tk.Tk()
    root.title('Whisper Audio Processing')

    tk.Label(root, text='Select Task:').grid(row=0, column=0)
    tk.Label(root, text='Select Language:').grid(row=1, column=0)

    task_var = tk.StringVar()
    task_var.set('transcribe')
    task_option = ttk.Combobox(root, textvariable=task_var, values=['transcribe', 'translate'])
    task_option.grid(row=0, column=1)

    language_var = tk.StringVar()
    language_var.set("English") # Default value set to English
    language_list = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Azerbaijani', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Castilian', 'Catalan', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Faroese', 'Finnish', 'Flemish', 'French', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Lao', 'Latin', 'Latvian', 'Letzeburgesch', 'Lingala', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Moldavian', 'Moldovan', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Nynorsk', 'Occitan', 'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Pushto', 'Romanian', 'Russian', 'Sanskrit', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Sinhalese', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uzbek', 'Valencian', 'Vietnamese', 'Welsh', 'Yiddish', 'Yoruba']
    language_option = ttk.Combobox(root, textvariable=language_var, values=language_list)
    language_option.grid(row=1, column=1)

    # Create an OptionMenu for "Select Report Type"
    report_type_var = tk.StringVar(root)
    report_type_var.set("all")  # default value
    tk.Label(root, text="Select Report Type").grid(row=2, column=0)
    tk.OptionMenu(root, report_type_var, "all", "txt", "srt", "json", "tsv", "vtt").grid(row=2, column=1)
    
     # Create an OptionMenu for "Model Choice"
    model_var = tk.StringVar(root)
    model_var.set("small")  # default value
    tk.Label(root, text="Select Language Model").grid(row=3, column=0)
    tk.OptionMenu(root, model_var, "small", "base", "medium", "large", "tiny").grid(row=3, column=1)
    
    def select_directories():
        global root  # Declare root as a global variable
        audio_directory = filedialog.askdirectory(title='Select Audio Directory')
        output_directory = filedialog.askdirectory(title='Select Output Directory')
        acceptable_extensions = ['.m4a', '.mp3', '.webm', '.mp4', '.mpga', '.wav', '.mpeg']
        process_audio_files(audio_directory, task_var.get(), language_var.get(), report_type_var.get(), model_var.get(), output_directory, acceptable_extensions)
        print("All audio files have been processed.")  # Notify that all processing is done
        exit()  # Close the Tkinter window 
    
    tk.Button(root, text='Select Directories and Start', command=select_directories).grid(row=6, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    main()



