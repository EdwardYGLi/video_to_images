import argparse
import os

import cv2
import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path",
        help="input path")
    parser.add_argument(
        "--output_path",
        help="output path",
        default="./output")
    parser.add_argument(
        "--show_visual",
        action="store_true")
    args = parser.parse_args()

    # make output directory
    output_path = args.output_path
    os.makedirs(output_path, exist_ok=True)

    # create video capture
    cap = cv2.VideoCapture(args.input_path)

    count = 0
    while cap.isOpened():
        # read frame
        ret, frame = cap.read()
        
        if not ret:
            break
        # write frame to file
        cv2.imwrite(
            os.path.join(
                output_path,
                "frame_{}.jpg".format(count)),
            frame)
        print("writing frame {} to {}".format(count, output_path))
        count += 1
        # show frame
        if args.show_visual:
            cv2.imshow("frame", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
