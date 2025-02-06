import os

# Directories containing the images
image_dir = os.path.join(os.path.dirname(__file__), 'Images')

# HTML template for the main page
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Illustruous-Artists</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #003366; /* Dark blue background */
            color: #d3d3d3; /* White-grey text color */
        }
        .prompt-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .prompt {
            padding: 10px;
            border-radius: 5px;
            width: 48%;
            box-sizing: border-box;
        }
        .positive-prompt {
            background-color: #228b22; /* Greenish background */
            color: #ffffff; /* White text color */
        }
        .negative-prompt {
            background-color: #b22222; /* Redish background */
            color: #ffffff; /* White text color */
        }
        .image-container {
            display: flex;
            flex-wrap: wrap;
        }
        .image-item {
            margin: 10px;
            width: 310px; /* Width to accommodate the image and border */
            box-sizing: border-box; /* Ensures padding and border are included in the element's total width and height */
        }
        img {
            max-width: 100%; /* Adjusted to fit within the container */
            height: auto;
            display: block;
            border: 3px solid #003366; /* Invisible border */
            transition: border 0.3s ease-in-out; /* Smooth transition for hover effect */
        }
        img:hover {
            border-color: #fef; /* Purple frame on hover */
        }
        .caption {
            text-align: center;
            margin-top: 5px;
        }
        .caption .artist-name {
            font-weight: bold; /* Bold artist name */
            color: #ffffff; /* White color for artist name */
        }
        .nav-link {
            color: #ffffff;
            margin: 20px 0;
            display: block;
            text-decoration: none;
            font-size: 18px;
        }
    </style>
    <script>
        function copyToClipboard(text) {
            const el = document.createElement('textarea');
            el.value = text;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            alert('Copied to clipboard: ' + text);
        }
    </script>
</head>
<body>
    <h1>Illustruous Artists</h1>
    <div class="prompt-container">
        <div class="prompt positive-prompt">
            <strong>Positive Prompt:</strong> 
            masterpiece, 4k, high quality, artist: Eigaka. 1girl, solo, Sakura, pink short hair, green eyes, forehead protector, blushing, looking at viewer, smiling, white dress, green background, gradient background
        </div>
        <div class="prompt negative-prompt">
            <strong>Negative Prompt:</strong> 
            worst quality, low quality, text, censored, blurry, (watermark), artist signature, artist name
        </div>
    </div>
    <a class="nav-link" href="combinations.html">View Artist Combinations</a>
    <a class="nav-link" href="classicArtists.html">View Classic Artist</a>
    <div class="image-container">
        {images}
    </div>
</body>
</html>
'''

# Generate HTML for individual artist images
image_html = ''
for filename in os.listdir(image_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Extract the artist name from the filename
        artist_name = filename.replace('_00001_', ' ').replace('.png', '').replace('.jpg', '').replace('.jpeg', '').replace('Artist-', '')
        image_html += f'''
        <div class="image-item">
            <img src="Images/{filename}" alt="{artist_name}" onclick="copyToClipboard('{artist_name}')">
            <div class="caption">
                <span class="artist">Artist:</span> <span class="artist-name">{artist_name}</span>
            </div>
        </div>
        '''

# Combine HTML template with images for main page
final_html = html_template.replace('{images}', image_html)

# Save the HTML file for the main page
output_path = os.path.join(os.path.dirname(__file__), 'index.html')
with open(output_path, 'w') as file:
    file.write(final_html)

print('index.html have been created')