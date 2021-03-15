from Base.Base import Base


class demonstrate(Base):
    def test_demo_1(self):
        logger = self.get_Logger()
        logger.info("running test_demo_1")
