#!/usr/bin/env python3

import pytube
import os
import argparse
from tqdm import tqdm

def download_video(url, output_path=None, resolution='highest'):
    """
    Download a YouTube video
    
    Args:
        url (str): YouTube video URL
        output_path (str, optional): Directory to save the video. Defaults to current directory.
        resolution (str, optional): Video resolution. Defaults to 'highest'.
                                    Options: 'highest', 'lowest', or specific resolution like '720p'
    
    Returns:
        str: Path to the downloaded video file
    """
    try:
        # Create a YouTube object
        yt = pytube.YouTube(url)
        
        # Add a progress bar callback
        def progress_callback(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            pbar.update(bytes_downloaded - pbar.n)
        
        yt.register_on_progress_callback(progress_callback)
        
        # Get the appropriate stream based on resolution
        if resolution == 'highest':
            stream = yt.streams.get_highest_resolution()
        elif resolution == 'lowest':
            stream = yt.streams.get_lowest_resolution()
        else:
            # Try to get the specific resolution
            stream = yt.streams.filter(res=resolution).first()
            if not stream:
                print(f"Resolution {resolution} not available. Using highest resolution.")
                stream = yt.streams.get_highest_resolution()
        
        # Prepare the output path
        if not output_path:
            output_path = os.getcwd()
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Initialize progress bar
        pbar = tqdm(total=stream.filesize, unit='B', unit_scale=True, 
                   desc=f"Downloading: {yt.title}")
        
        # Download the video
        file_path = stream.download(output_path)
        
        # Close progress bar
        pbar.close()
        
        print(f"\nDownload complete! Video saved to: {file_path}")
        return file_path
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download YouTube videos')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-o', '--output', help='Output directory path', default=None)
    parser.add_argument('-r', '--resolution', help='Video resolution (highest, lowest, or specific like 720p)', 
                       default='highest')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Download the video
    download_video(args.url, args.output, args.resolution)

if __name__ == '__main__':
    main()