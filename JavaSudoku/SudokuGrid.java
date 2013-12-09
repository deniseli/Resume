/*
 * DISCLAIMER: I wrote this class as a junior in high school so there's a hell
 * of a lot of ugly and repeated code.  I'll fix it if I have time at some point
 * but for now, there's a much better python version at ../Sudoku.py
 * Anyway, here's the naive solution.  If you're 15 years old, you'll probably
 * think it's cool.
 */


public class SudokuGrid
{
	private String[][] grid;
	public SudokuGrid(String s)
	{
		grid = new String[9][9];
		//fill all
		for(int r=0; r<9; r++)
			for(int c=0; c<9; c++)
				grid[r][c] = "123456789";
		//sets given nodes
		//i know they aren't called nodes but w/e
		for(int r=0; r<9; r++)
			for(int c=0; c<9; c++)
				if(s.charAt(r*9+c)!='0')
					grid[r][c] = ""+s.charAt(r*9+c);
		System.out.println("INCOMPLETE:\n"+toString());
		//keep removing as long as you can
		recSimplify();
		System.out.println("\n\nCOMPLETE:\n"+toString());
	}
	public void recSimplify()
	{
		//call recSimplify again if a change is made
		boolean changed = false;
		if(checkColumns())
			changed = true;
		if(checkRows())
			changed = true;
		if(checkSquares())
			changed = true;
		if(changed)
			recSimplify();
	}
	public boolean checkColumns()
	{
		boolean changed = false;
		//get rid of impossible
		for(int r=0; r<9; r++)
			for(int c=0; c<9; c++)
				for(int r2=0; r2<9; r2++)
					if(r!=r2&&grid[r][c].length()==1&&removeNumber(r2, c, Integer.parseInt(grid[r][c])))
						changed = true;
		//set necessary
		int count = 0;
		int loc = 0;
		for(int c=0; c<9; c++)
		{
			//i is number to check for
			for(int i=1; i<=9; i++)
			{
				for(int r=0; r<9; r++)
					if(grid[r][c].contains(i+""))
					{
						count++;
						loc = r;
					}
				if(count==1)
				{
					if(grid[loc][c].length()>1)
						changed = true;
					grid[loc][c] = i+"";
				}
				count = 0;
			}		
		}
		return changed;
	}
	public boolean checkRows()
	{
		boolean changed = false;
		//get rid of impossible
		for(int r=0; r<9; r++)
			for(int c=0; c<9; c++)
				for(int c2=0; c2<9; c2++)
					if(c!=c2&&grid[r][c].length()==1&&removeNumber(r, c2, Integer.parseInt(grid[r][c])))
						changed = true;
		//set necessary
		int count = 0;
		int loc = 0;
		for(int r=0; r<9; r++)
		{
			//i is number to check for
			for(int i=1; i<=9; i++)
			{
				for(int c=0; c<9; c++)
					if(grid[r][c].contains(i+""))
					{
						count++;
						loc = c;
					}
				if(count==1)
				{
					if(grid[r][loc].length()>1)
						changed = true;
					grid[r][loc] = i+"";
				}
				count = 0;
			}		
		}
		return changed;
	}
	public boolean checkSquares()
	{
		boolean changed = false;
		int count = 0;
		String loc = "";
		for(int r=0; r<9; r+=3)
			for(int c=0; c<9; c+=3)
			{
				//get rid of impossible
				//loops for each square
				for(int r2=r; r2<r+3; r2++)
					for(int c2=c; c2<c+3; c2++)
					{
						//do this thing.
						for(int r3=r; r3<r+3; r3++)
							for(int c3=c; c3<c+3; c3++)
								if(r2!=r3&&c2!=c3&&grid[r2][c2].length()==1&&removeNumber(r3, c3, Integer.parseInt(grid[r2][c2])))
									changed = true;
					}
				//set necessary
				//i is number being checked for
				for(int i=1; i<=9; i++)
				{
					for(int r2=r; r2<r+3; r2++)
						for(int c2=c; c2<c+3; c2++)
							if(grid[r2][c2].contains(i+""))
							{
								count++;
								loc = r2+""+c2;
							}
					if(count==1)
					{
						if(grid[Integer.parseInt(""+loc.charAt(0))][Integer.parseInt(""+loc.charAt(1))].length()>1)
							changed = true;
						grid[Integer.parseInt(""+loc.charAt(0))][Integer.parseInt(""+loc.charAt(1))] = i+"";
					}
					count = 0;
				}
			}
		return changed;
	}
	private boolean removeNumber(int r, int c, int toRemove)
	{
		if(grid[r][c].contains(""+toRemove))
		{
			int place = grid[r][c].indexOf(""+toRemove);
			grid[r][c] = grid[r][c].substring(0, place)+
				grid[r][c].substring(place+1, grid[r][c].length());
			return true;
		}
		return false;
	}
	public String toString()
	{
		String s = "";
		for(int r=0; r<9; r++)
		{
			if(r%3==0)
				s+="\n";
			for(int c=0; c<9; c++)
			{
				if(grid[r][c].length()==1)
					s+=grid[r][c]+"";
				else
					s+="_";
				if(c%3==2)
					s+="    ";
				else
					s+=" ";
			}
			s+="\n";
		}
		return s;
	}
}