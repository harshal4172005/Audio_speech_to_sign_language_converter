import speech_recognition as sr
from PIL import Image
import imageio
import matplotlib.pyplot as plt

# Step 1: Create a dictionary that maps each letter and some words to their image or GIF file paths
sign_language_dict = {
    "A": "A to Z/A.jpg",
    "B": "A to Z/B.jpg",
    "C": "A to Z/C.jpg",
    "D": "A to Z/D.jpg",
    "E": "A to Z/E.jpg",
    "F": "A to Z/F.jpg",
    "G": "A to Z/G.jpg",
    "H": "A to Z/H.jpg",
    "I": "A to Z/I.jpg",
    "J": "A to Z/J.jpg",
    "K": "A to Z/K.jpg",
    "L": "A to Z/L.jpg",
    "M": "A to Z/M.jpg",
    "N": "A to Z/N.jpg",
    "O": "A to Z/O.jpg",
    "P": "A to Z/P.jpg",
    "Q": "A to Z/Q.jpg",
    "R": "A to Z/R.jpg",
    "S": "A to Z/S.jpg",
    "T": "A to Z/T.jpg",
    "U": "A to Z/U.jpg",
    "V": "A to Z/V.jpg",
    "W": "A to Z/W.jpg",
    "X": "A to Z/X.jpg",
    "Y": "A to Z/Y.jpg",
    "Z": "A to Z/Z.jpg",
    # Word examples
    "MORNING": "words/morning.gif",
    "DANCE": "words/dance.gif",
    "DEAD": "words/dead.gif",
    "DEAF": "words/deaf.gif",
    "FAMILY": "words/family.gif",
    "FOOD": "words/food.gif",
    "HELLO": "words/hello.gif",
    "JALAPENO": "words/jalapeno.gif",
    "NO": "words/no.gif",
    "PASTA": "words/pasta.gif",
    "PLEASE": "words/please.gif",
    "WEEKEND": "words/weekend.gif",
    # Sentence examples
    "GOOD AFTERNOON": "Sentences/good afternoon.gif",
    "GOOD EVENING": "Sentences/good evening.gif",
    "GOOD MORNING": "Sentences/good morning.gif",
    "GOOD NIGHT": "Sentences/good night.gif",
    "HOW ARE YOU DOING": "Sentences/how are you doing.gif",
    "I DON'T UNDERSTAND": "Sentences/i don_t understand.gif",
    "I'LL HELP YOU": "Sentences/i_ll help you.gif",
    "WHAT ARE YOU DOING": "Sentences/what are you doing.gif",
    "WHAT'S UP": "Sentences/what_s up.gif",
}

# Step 2: Function to display the image or GIF for each letter/word
def display_sign_image(item):
    item = item.upper()  # Convert to uppercase to match the dictionary keys
    if item in sign_language_dict:
        image_path = sign_language_dict[item]
        try:
            if image_path.endswith('.gif'):
                play_gif(image_path)
            else:
                img = Image.open(image_path)
                img.show()  # Display the image
        except FileNotFoundError:
            print(f"Image or GIF not found for: {item}")
    else:
        print(f"No sign image or GIF available for: {item}")

# Function to play GIFs using imageio and matplotlib
def play_gif(gif_path):
    gif = imageio.mimread(gif_path)
    fig = plt.figure()

    # Loop through frames
    for frame in gif:
        plt.imshow(frame)
        plt.axis('off')
        plt.pause(0.1)  # Adjust the speed of playback

    plt.show()

# Step 3: Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to the microphone
        try:
            # Convert speech to text using Google's speech recognition
            recognized_text = recognizer.recognize_google(audio)
            print(f"You said: {recognized_text}")
            return recognized_text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
    return None

# Step 4: Process the recognized text and display images for each letter
recognized_text = speech_to_text()
if recognized_text:
    # Normalize the text for matching
    recognized_text = recognized_text.upper()  # Convert recognized text to uppercase
    # First check if the entire sentence is in the dictionary
    display_sign_image(recognized_text)
    
    # If the sentence is not found, split the recognized text into words
    words = recognized_text.split()
    for word in words:
        display_sign_image(word)  # Display each word's GIF/image
