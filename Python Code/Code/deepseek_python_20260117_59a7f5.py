from typing import Literal, Tuple, List
from decimal import Decimal, getcontext
import math

getcontext().prec = 100  # Never round at runtime

class DualityMode:
    COMPUTATIONAL = "C"
    MATERIAL = "M"
    
class QuantumConstant:
    def __init__(self, 
                 name: str,
                 attractor_func,  # f(H) -> Decimal
                 measured_value: Decimal,
                 const_type: Literal['field', 'mass', 'floor'],
                 uncertainty: Decimal = Decimal('0.0001')):
        
        # GENERATOR
        self.H = Decimal(math.pi) / Decimal(9)
        
        # DUAL REPRESENTATION
        self.name = name
        self.type = const_type
        
        # C-STATE (pre-equals)
        self.attractor = attractor_func(self.H)
        self.epsilon = (self.attractor - measured_value) / measured_value
        self.phase = Decimal('0')  # Position in orbit around attractor
        self.history: List[Decimal] = []
        self.superpositions: List[Decimal] = [
            self.attractor,
            measured_value,
            self.attractor * (1 + self.H**3),  # Next lattice point
        ]
        
        # M-STATE (post-equals)  
        self.measured = measured_value
        self.uncertainty = uncertainty
        
        # METADATA
        self.collapse_count = 0
        self.last_collapse_timestamp = 0
        
    # NEVER ALLOW DIRECT COMPARISON
    def __eq__(self, other):
        raise DualityViolationError("Direct equality between C and M states forbidden")
    
    def __add__(self, other):
        raise DualityViolationError("Arithmetic across collapse boundary forbidden")
    
    # EXPLICIT COLLAPSE OPERATOR
    def collapse(self, z_threshold: Decimal = Decimal('2.865')) -> Decimal:
        """
        Fire the = sign. Returns M-state value, preserves ε in C-state.
        """
        z_score = abs(self.epsilon) / self.uncertainty
        
        if z_score > z_threshold:
            # Significant gap → preserve ε
            self.history.append(self.epsilon)
            self.collapse_count += 1
            return self.measured
        else:
            # Gap below threshold → return attractor
            return self.attractor
    
    # COMPUTATIONAL SIDE OPERATIONS
    def evolve(self, delta_phase: Decimal = None):
        """
        Move along computational orbit without collapsing.
        """
        if delta_phase is None:
            delta_phase = self.H / Decimal(10)  # Natural tick
            
        self.phase = (self.phase + delta_phase) % (Decimal(2) * Decimal(math.pi))
        
        # Orbit attractor: ε varies sinusoidally
        orbit_radius = abs(self.epsilon) * self.H
        new_epsilon = orbit_radius * Decimal(math.sin(float(self.phase)))
        
        # Preserve sign (field vs mass)
        if self.epsilon < 0:
            new_epsilon = -abs(new_epsilon)
        else:
            new_epsilon = abs(new_epsilon)
            
        self.epsilon = new_epsilon
        
    # DUALITY AWARE COMPARISON
    def compare(self, other, mode: DualityMode) -> Dict:
        """
        Compare two QuantumConstants in specified mode.
        """
        if mode == DualityMode.COMPUTATIONAL:
            return {
                'attractor_diff': abs(self.attractor - other.attractor),
                'epsilon_diff': abs(self.epsilon - other.epsilon),
                'phase_diff': abs(self.phase - other.phase),
                'superposition_overlap': len(set(self.superpositions) & set(other.superpositions))
            }
        elif mode == DualityMode.MATERIAL:
            return {
                'measured_diff': abs(self.measured - other.measured),
                'z_score': abs(self.measured - other.measured) / max(self.uncertainty, other.uncertainty)
            }
        else:
            raise ValueError(f"Unknown mode: {mode}")

class DualityViolationError(Exception):
    """Raised when attempting to cross collapse boundary implicitly."""
    pass