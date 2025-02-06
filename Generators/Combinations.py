import os

# Directories containing the images
combo_image_dir = os.path.join(os.path.dirname(__file__), 'CombinedArtists')

# HTML template for the combinations page
combo_html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artist Combinations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #003366; /* Dark blue background */
            color: #d3d3d3; /* White-grey text color */
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
    <h1>Artist Combinations</h1>
    <a class="nav-link" href="index.html">Back to Main Page</a>
    <a class="nav-link" href="classicArtists.html">View Classic Artist</a>
    <div class="image-container">
        {images}
    </div>
</body>
</html>
'''

# Generate HTML for combination images
combo_image_html = ''
for filename in os.listdir(combo_image_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Extract the artist names from the filename
        artist_names = filename.replace('_00001_', ' ').replace('.png', '').replace('.jpg', '').replace('.jpeg', '').replace('Artist-', '')
        combo_image_html += f'''
        <div class="image-item">
            <img src="CombinedArtists/{filename}" alt="{artist_names}" onclick="copyToClipboard('{artist_names}')">
            <div class="caption">
                <span class="artist">Artists:</span> <span class="artist-name">{artist_names}</span>
            </div>
        </div>
        '''

# Combine HTML template with images for combinations page
final_combo_html = combo_html_template.replace('{images}', combo_image_html)

# Save the HTML file for the combinations page
combo_output_path = os.path.join(os.path.dirname(__file__), 'combinations.html')
with open(combo_output_path, 'w') as file:
    file.write(final_combo_html)

print('combinations.html have been created')