class IEC60601SafetyGuard:
    @staticmethod
    def clamp_current(raw_pwm: int) -> int:
        # Max limit corresponding to <448.5 uA
        return min(raw_pwm, 210)
