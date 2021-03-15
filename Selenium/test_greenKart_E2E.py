from Base.Base import Base


class green_Kart(Base):
    def purchase(self):
        logger = self.get_Logger()
        logger.info("Green Kart Items has been Purchased")
