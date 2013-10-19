CrosswordDetectorSolver
=======================
//===============================//
// Authors
//===============================//
  Robert Chang
  Rohan Chitnis
  Harrison Wang
  Sydney Wong

//===============================//
// Description
//===============================//
  Libraries used: CImg, BeautifulSoup, Image Magick, Tesseract

  Given an image of a crossword, process the image and display the solved crossword puzzle.

//===============================//
// Instructions
//===============================//
  To use CrosswordDetectorSolver, you first take a picture of the crossword puzzle board and pictures of the clues.
  CImg will read in the image of the board and decide if a certain cell is black and white. The picture is assumed to be cropped and can be slightly slanted.
  A display will show up with the solved crossword puzzle.

//===============================//
// Further description
//===============================//
  After the clues are parsed, they are inputted as search values into three crossword-puzzle clue/answer websites, crosswordnexus.com, crosswordheaven.com, and crosswordtracker.com.  First we studied the urls from the different websites to write urls for our clues.  We used python to read the html from the different websites and to create lists of possible answers (that met our length requirement and were not duplicates) to the clue. 

  Then we wrote an algorithm that puts clue numbers in their respective blocks for the output board.   
 
