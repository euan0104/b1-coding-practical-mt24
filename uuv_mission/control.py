# control.py
class PDController:
    def __init__(self, KP=0.15, KD=0.6):
        # Initialize the proportional (KP) and derivative (KD) gains
        self.KP = KP
        self.KD = KD
        # Initialize the previous error to zero
        self.previous_error = 0

    def compute_control_action(self, reference, output):
        # Calculate the current error
        error = reference - output
        # Calculate the derivative of the error
        derivative = error - self.previous_error
        # Compute the control action using the PD formula
        control_action = self.KP * error + self.KD * derivative
        # Update the previous error for the next iteration
        self.previous_error = error
        return control_action