using System;

namespace KulikFormulaExample
{
    class FractalGrowthSimulation
    {
        public static void Main()
        {
            int gridSize = 10;
            double growthThreshold = 0.5;

            double[,] grid = InitializeGrid(gridSize);
            SimulateGrowth(grid, growthThreshold);

            Console.WriteLine("Fractal Growth Simulation:");
            DisplayGrid(grid);
        }

        private static double[,] InitializeGrid(int size)
        {
            var random = new Random();
            double[,] grid = new double[size, size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    grid[i, j] = random.NextDouble(); // Random potential values
                }
            }

            return grid;
        }

        private static void SimulateGrowth(double[,] grid, double threshold)
        {
            int size = grid.GetLength(0);

            for (int i = 1; i < size - 1; i++)
            {
                for (int j = 1; j < size - 1; j++)
                {
                    double harmonicSum = grid[i - 1, j] + grid[i + 1, j] +
                                         grid[i, j - 1] + grid[i, j + 1];

                    if (harmonicSum / 4.0 > threshold)
                    {
                        grid[i, j] = 1.0; // Growth occurs
                    }
                }
            }
        }

        private static void DisplayGrid(double[,] grid)
        {
            int size = grid.GetLength(0);

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    Console.Write(grid[i, j] >= 1.0 ? "X " : ". ");
                }
                Console.WriteLine();
            }
        }
    }
}
