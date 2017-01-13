package com.test;
import java.util.ArrayList;
import java.util.HashMap;

public class Restaurant {
	public static void main(String[] args) {
		HashMap<String,Integer> restaurantMenu = new HashMap<String, Integer>();
	    restaurantMenu.put("Turkey Burger",13);
	    restaurantMenu.put("Naan Pizza",11);
	    System.out.println(restaurantMenu.get("Naan Pizza"));
	    
	    
		ArrayList<Integer> weeklyTemperatures = new ArrayList<Integer>();
		weeklyTemperatures.add(78);
		weeklyTemperatures.add(67);
		weeklyTemperatures.add(89); 
		weeklyTemperatures.add(94);
		
		for (Integer temperature : weeklyTemperatures ) {
			System.out.println(temperature);
		}
		for (int i=0;i<weeklyTemperatures.size();i++){
			System.out.println(i);
		}
	}
}