const AbstractPage = require('./abstract_page');

class FlightPage extends AbstractPage {

  constructor(page) {
    super(page);
  }

  async selectTripType(trip_type) {
    const radios = await this.page.$$("input[name=tripType]");
    if (trip_type == "oneway") {
      await radios[1].check();
    } else  {
        await radios[0].check();
    }
  }

  async selectDepartFrom(city) {
    await this.page.selectOption("select[name='fromPort']", city);
  }

  async selectArriveAt(city) {
    await this.page.selectOption("select[name='toPort']", city);
  }

  async selectDepartDay(day) {
    await this.page.selectOption("select[name='departDay']", day);
  }

  async selectDepartMonth(month_year) {
     await this.page.selectOption("#departMonth", month_year);
  }

  async selectReturnDay(day) {
    await this.page.selectOption("select[name='returnDay']", day);

  }

  async selectReturnMonth(month_year) {
    await this.page.selectOption("#returnMonth", month_year);
  }

  async clickContinue() {
    await this.page.click("input:has-text('Continue')");
  }
};

module.exports = FlightPage;
