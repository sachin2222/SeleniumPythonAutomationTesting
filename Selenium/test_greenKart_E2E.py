from Base.Base import Base


class Testdemo(Base):
    def test_purchase(self):
        log = self.get_Logger()
        log.info("Test_Purchase Executed")
        log.error("Error Message")
        assert 1 == 2, "values are not Equal"
