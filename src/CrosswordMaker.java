
import java.awt.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import javax.swing.*;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Is supposed to create the crossword itself. Adds the letters based on input
 * words.
 *
 * @author Robert
 */
public class CrosswordMaker extends JFrame {

    public static final int VERTICAL = 1;
    public static final int HORIZONTAL = 0;
    
    /***
     * Gets a list of characters and prints them to the graph
     * @param characterList refers to the list of characters.
     */
    public CrosswordMaker(ArrayList<Character> characterList) {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JLayeredPane p = new JLayeredPane();
        Letters letters = new Letters();
        int count = 0;
        for (Character character : characterList) {
            letters.addLetter(character.getCharacter(),character.getx() * 20, character.gety() * 20);
        }
        add(letters);
        pack();
        setLocationRelativeTo(null);
        setVisible(true);

    }

    public static void main(String[] args) throws IOException {
        File file = new File("numbers.txt");
        ArrayList<Character> letterList = CrosswordMaker.parser(file);
        ArrayList<Word> wordList = new ArrayList<Word>();
        new CrosswordMaker(letterList);
    }

    /**
     * Interprets a file in the format character x y per line. This allows me to generate a list of characters.
     * @param file
     * @return
     * @throws FileNotFoundException
     * @throws IOException 
     */
    public static ArrayList<Character> parser(File file) throws FileNotFoundException, IOException {
        
        ArrayList<Character> letterList = new ArrayList<Character>();
        BufferedReader br = new BufferedReader(new FileReader(file));
        String line = null;
        while ((line = br.readLine()) != null) {
             String[] a = line.split(" ");
             letterList.add(new Character(a[0],new Integer(a[1]),new Integer(a[2])));
        }
        return letterList;    
    }
}
/***
 * This letters class is to actually paint them on the GUI.
 * @param letter refers to the letter inserted.
 * @param x_axis takes x values.
 * @param y_axis takes y values.
 * @author Robert
 */
class Letters extends JPanel {

    private static final int PREF_W = 500;
    private static final int PREF_H = PREF_W;
    public int[][] squares = new int[100][100];
    private ArrayList<String> letter = new ArrayList<String>();
    private ArrayList<Integer> x_axis = new ArrayList<Integer>();
    private ArrayList<Integer> y_axis = new ArrayList<Integer>();

    /***
 * This adds a letter.
 * @params: x coordinate, y coordinate, letter.
 * @author Robert
 */
    public void addLetter(String character, int x, int y) {
        letter.add(character);
        x_axis.add(x);
        y_axis.add(y);
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(PREF_W, PREF_H);
    }

    /***
 * This algorithm prints the actual picture to the GUI. In the case where a box isn't filled
 * by the end of the function, the box will be filled black.
 * @param g is the graphics interface the program uses.
 * @author Robert
 */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        this.setFont(new Font("TimesRoman", Font.BOLD, 20));
        Graphics2D g2 = (Graphics2D) g;
        System.out.println(letter.size());
        for (int i = 0; i < letter.size(); i++) {
            squares[x_axis.get(i) / 20][ y_axis.get(i) / 20] = 1;
	    if(letter.get(i) == "None"){
		continue;
	    }
            g.setColor(Color.RED);
            g2.drawString(letter.get(i), x_axis.get(i) + 2, y_axis.get(i) + 20);
            g.setColor(Color.BLACK);
            Rectangle r = new Rectangle(x_axis.get(i), y_axis.get(i), 20, 20);
            g2.draw(r);
        }
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (squares[i][j] == 0) {
                    g2.fillRect(i * 20, j * 20, 20, 20);
                }
            }
        }

    }
}
