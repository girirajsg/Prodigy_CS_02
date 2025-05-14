from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGBA')  # Ensure image has RGBA channels
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b, a)

    img.save(output_path)
    print("✅ Image encrypted and saved successfully.")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGBA')
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b, a)

    img.save(output_path)
    print("✅ Image decrypted and saved successfully.")

def main():
    print("🔐 Image Encryption Tool")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("❌ Invalid choice.")
        return

    input_path = input("Enter input image path (e.g. input.png): ").strip().strip('"')
    output_path = input("Enter output image path (e.g. output.png): ").strip().strip('"')
    try:
        key = int(input("Enter a numeric key (e.g. 10): "))
    except ValueError:
        print("❌ Invalid key. Must be an integer.")
        return

    try:
        if choice == 'encrypt':
            encrypt_image(input_path, output_path, key)
        else:
            decrypt_image(input_path, output_path, key)
    except FileNotFoundError:
        print("❌ Input image not found!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
