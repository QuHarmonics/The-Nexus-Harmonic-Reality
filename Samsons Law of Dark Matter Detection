using System;
using System.Collections.Generic;
using System.Linq;

namespace KulikFormula.DarkMatterDetection
{
    public class SamsonLaw
    {
        public double GravitationalConstant { get; set; } = 6.67430e-11; // in m^3⋅kg^−1⋅s^−2
        public double DetectionThreshold { get; set; } = 0.0001;

        public List<HarmonicDensity> DetectHarmonics(List<GravitationalBody> bodies)
        {
            var detectedDensities = new List<HarmonicDensity>();

            foreach (var body in bodies)
            {
                double density = CalculateHarmonicDensity(body);

                if (density >= DetectionThreshold)
                {
                    detectedDensities.Add(new HarmonicDensity
                    {
                        Body = body,
                        Density = density
                    });
                }
            }

            return detectedDensities;
        }

        public double EstimateDarkMatterMass(double observedGravity, double expectedGravity)
        {
            return (observedGravity - expectedGravity) / GravitationalConstant;
        }

        private double CalculateHarmonicDensity(GravitationalBody body)
        {
            return body.Mass / (body.Distance * body.Distance);
        }
    }

    public class GravitationalBody
    {
        public string Name { get; set; }
        public double Mass { get; set; }
        public double Distance { get; set; }
        public double ObservedGravity { get; set; }
        public double ExpectedGravity { get; set; }
    }

    public class HarmonicDensity
    {
        public GravitationalBody Body { get; set; }
        public double Density { get; set; }
    }

    public class Program
    {
        static void Main()
        {
            var bodies = new List<GravitationalBody>
            {
                new GravitationalBody { Name = "Object1", Mass = 5.972e24, Distance = 1.0e7, ObservedGravity = 9.8, ExpectedGravity = 9.5 },
                new GravitationalBody { Name = "Object2", Mass = 1.989e30, Distance = 1.5e11, ObservedGravity = 1.0, ExpectedGravity = 0.95 }
            };

            var samsonLaw = new SamsonLaw();
            var detectedHarmonics = samsonLaw.DetectHarmonics(bodies);

            Console.WriteLine("Detected Harmonic Densities:");
            foreach (var density in detectedHarmonics)
            {
                Console.WriteLine($"Body: {density.Body.Name}, Harmonic Density: {density.Density}");
            }

            Console.WriteLine("\nEstimating Dark Matter Contribution:");
            foreach (var body in bodies)
            {
                var darkMatterMass = samsonLaw.EstimateDarkMatterMass(body.ObservedGravity, body.ExpectedGravity);
                Console.WriteLine($"Body: {body.Name}, Estimated Dark Matter Mass: {darkMatterMass}");
            }
        }
    }
}
