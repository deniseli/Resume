public class SudokuRunner
{
	public static void main(String[]args)
	{
		String sendIn = "";
		
//		sendIn+="249678153";
//		sendIn+="137524869";
//		sendIn+="865319274";
//		
//		sendIn+="924867315";
//		sendIn+="378152496";
//		sendIn+="516493782";
//		
//		sendIn+="652731948";
//		sendIn+="491285637";
//		sendIn+="783946521";
		
		sendIn+="049608100";
		sendIn+="000020069";
		sendIn+="005000204";
		
		sendIn+="000060000";
		sendIn+="300102000";
		sendIn+="016093080";
		
		sendIn+="600031040";
		sendIn+="091000630";
		sendIn+="003040500";
		
		if(sendIn.length()==81)
			new SudokuGrid(sendIn);
	}
}