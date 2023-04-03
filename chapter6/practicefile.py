def main():

    videos = int(input("Get the number of   videos in the project."))
    
    # Open an output file.
    video_file = open('videosTimesText.txt', 'w')
    print('Enter the running times for each video.')
    # For each video in the project:
    for count in range(1,videos+1):
            # Get the video's running time.
        run_time = float(input(f'Video #{count}: '))
            # Write the running time to the file.
        video_file.write(f'{run_time}')

        # Close the file.
    videos.close()

# Call the main function.
if __name__ == '__main__':
    main()

