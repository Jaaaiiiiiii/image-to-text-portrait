from PIL import Image, ImageDraw, ImageFont
# Importing tools.

IMAGE_PATH = r"YOUR FILE HERE"
# The image we want to convert. 
# (ADDITIONAL TIP: U CAN "COPY AS PATH" YOUR FILE FOR EASY LOCATING)
# Right-click your image file -> "Copy as path" -> Paste it!
# Wag pahirapan ang sarili mag type manually, copy paste lang yan boi!

TEXT = "I Love You"
# The text we want to put.

OUTPUT_WIDTH = 4000
# Resolution in short, no need to understand. Parang 4k resolution ganon.

def draw_detailed_portrait():

    print(f"1. Loading image...")
    # Even though unnecessary this, we can use it as an indicator that it's now processing...

    clean_path = IMAGE_PATH.replace('"', '')
    # We just created this to escape the file path quotes.

    try:
        img = Image.open(clean_path).convert("L")
        # We insert to img yung clean na path sa file then we open it and convert to Luminance (tanggal rgb).

    except:
        print("ERROR: Could not find file!")
        # Pag di nahanap, mag-indicate na file not found.
        
        return
        # Exit the draw_detailed_portrait function immediately.

    width, height = img.size
    # Width and height comes from the image file itself (coming from the Image.open; it stores to img the width and height).

    new_height = int(OUTPUT_WIDTH * height / width)
    # We now adapt.

    img = img.resize((OUTPUT_WIDTH, new_height))
    # 4000 TIMES THE New Dimension we want (this is the recommended dimension, para clear siya boi).
    
    
    canvas = Image.new('RGB', (OUTPUT_WIDTH, new_height), 'black')
    # Eto na yung sketchpad natin, may filter na yan black para eyyable. Next ko yung colored version!

    draw = ImageDraw.Draw(canvas)
    # Eto na yung drawer natin, siya na bahala mag draw. Mag drawing na siya sa canvas (yung sketchpad natin kanina).
   
    font_size = 12 
    # Sabi nila the more font the more details e!

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
        # Font lang toh gaiz.
    except:
        font = ImageFont.load_default()
        # Pag may nag error etong default nlng! (wag nmn uy!).

    print("2. Drawing thousands of words... (This might take 20-30 seconds)")
    # Pampakulo sayo, de joke lang. It's for indicator again that it's now successfully working and passed the functions above eyyy!!!
    
    pixels = img.load()
    text_idx = 0
    # Si pixels susi, si text index sha yung counter kung sang letter na ba (declaration).

    step_x = 8 
    step_y = 8
    # 8 pixel lang magiging space para pagka zoomout eyyable yan boi!!!

    for y in range(0, new_height, step_y):
        for x in range(0, OUTPUT_WIDTH, step_x):
            if x < OUTPUT_WIDTH and y < new_height:
                brightness = pixels[x, y]
                # Outer loop y vertical pababa 8 pixels space.
                # Inner loop x horizontal left to right 8 pixels space ulit.
                # 8 para di patong patong, there's room for space eyy.
                # Brightness = pixels mo sa x and y check ba if may shadow tas mag aadapt nalang magic e.
                
                # If it's pitch black, don't draw anything (saves time).
                if brightness > 5:

                    char = TEXT[text_idx % len(TEXT)]
                    """
                    Tapos yung char basta formula yan sha modulo operator in which counter index % how 
                    many characters in ILoveYou, kung ano remainder yun corresponding number pupuntahan for 0 is I, 1 is L 
                    and so on and so forth hanggang bumalik sa I ulit.
                    """
       
                    draw.text((x, y), char, fill=(brightness, brightness, brightness), font=font)
                    """
                    draw.text is a built-in function again to draw at exact coordinate of x and y 
                    incrementing. While incrementing, we put the character simultaneously 
                    and the color is magic and adjusting accordingly.
                    """
                
                text_idx += 1
                # Increment
   
    canvas.save("cutie.jpg")
    # Kaw na bahala if ano file name want mo.
    print("3. DONE! Open 'cutie.jpg'.")
    # Indicator ulit.

draw_detailed_portrait()
