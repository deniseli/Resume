import java.util.ArrayList;

public class SudokuGrid3D
{
	private String[][][] grid = new String[9][9][9];
	public SudokuGrid3D(String input)
	{
		for(int x=0; x<9; x++)
			for(int y=0; y<9; y++)
				for(int z=0; z<9; z++)
				{
					if(input.charAt(x*81 + y*9 + z)=='0')
						grid[x][y][z] = "123456789";
					grid[x][y][z] = ""+input.charAt(x*81 + y*9 + z);
				}
	}
	private void recSimplify()
	{
		
	}
	public boolean isDefined(int x, int y, int z)
	{
		return grid[x][y][z].length() == 1;
	}
	public ArrayList<String> getDefinedPeers(int x, int y, int z)
	{
		ArrayList<String> peers = new ArrayList<String>();
		//rows, columns, depths
		for(int i=0; i<9; i++)
		{
			if(isDefined(x,y,i) && i!=z)
				peers.add(grid[x][y][i]);
			if(isDefined(x,i,z) && i!=y)
				peers.add(grid[x][i][z]);
			if(isDefined(i,y,z) && i!=x)
				peers.add(grid[i][y][z]);
		}
		//3x3 blocks
		int x0 = x - x%3;
		int y0 = y - y%3;
		int z0 = z - z%3;
		for(int i=x0; i<x0+3; i++)
			for(int j=y0; j<y0+3; j++)
				if(isDefined(i,j,z) && (i!=x && j!=y))
					peers.add(grid[i][j][z]);
		for(int i=x0; i<x0+3; i++)
			for(int j=z0; j<z0+3; j++)
				if(isDefined(i,y,j) && (i!=x && j!=z))
					peers.add(grid[i][y][j]);
		for(int i=y0; i<y0+3; i++)
			for(int j=z0; j<z0+3; j++)
				if(isDefined(x,i,j) && (i!=y && j!=z))
					peers.add(grid[x][i][j]);
		
		return peers;
	}
	public boolean removeValue(String value, int x, int y, int z)
	{
		if(!grid[x][y][z].contains(value))
			return false;
		int r = grid[x][y][z].indexOf(value);
		grid[x][y][z] = grid[x][y][z].substring(0,r) +
				grid[x][y][z].substring(r+1,grid[x][y][z].length());
		return true;
	}
	private boolean removeImpossible(int x, int y, int z)
	{
		ArrayList<String> peers = getDefinedPeers(x,y,z);
		boolean changed = false;
		for(String peer: peers)
		{
			if(removeValue(peer, x, y, z))
				changed = true;
		}
		return changed;
	}
}