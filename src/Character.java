/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Robert
 */
public class Character {
    private String character;
    private int x;
    private int y;
    /**
    * Constructor for word. 
    * @params (x,y) coordinates, character parameter.
    * length of word
    * @author Robert
    */
    public Character(String character, int x, int y){
        this.x = x;
        this.y = y;
        this.character = character;
        
    }
    /*
    Gets the value of x.
    @return x
    */
    public int getx(){
        return x;
    }
    /*
    Gets the value of y.
    @return x
    */
    public int gety(){
        return y;
    }
    /*
    Gets the value of answer.
    @return x
    */
    public String getCharacter(){
        return character;
    }
}
