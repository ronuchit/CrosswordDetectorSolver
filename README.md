CrosswordDetectorSolver
=======================

Given an image of a crossword, process the image and return the solved crossword puzzle.

Libraries we used: CImg, BeautifulSoup, Image Magick, Tesseract

To use the CrosswordDetectorSolver, you first take a picture of the crossword puzzle board and pictures of the clues.  Then we used CImg to "read in" the image of the board.  To decide if a "block" was black or white, we took a random sample of the pixels in that block and, if the average number of black pixels was over a certain threshold, we decided that block was black.  This process required some photo-editing to get rid of the numbers in the corners of certain white blocks (in which there are more black pixels than the average completely white block).

After you have parsed the clues, they are inputted as search values into three crossword-puzzle clue/answer websites, crosswordnexus.com, crosswordheaven.com, and crosswordtracker.com.  First we studied the urls from the different websites to write urls for our clues.  We used python to read the html from the different websites and to create lists of possible answers (that met our length requirement and were not duplicates) to the clue. 

Then we wrote an algorithm that puts clue numbers in their respective blocks for the output board.   
 
