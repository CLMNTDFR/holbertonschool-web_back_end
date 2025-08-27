const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
    let spyConsole;

    beforeEach(function() {
        spyConsole = sinon.spy(console, 'log');
    });

    afterEach(function() {
        spyConsole.restore();
    });

    it('should log "The total is: 120" when called with 100 and 20', function() {
        sendPaymentRequestToApi(100, 20);
        expect(spyConsole.calledWith('The total is: 120')).to.be.true;
        expect(spyConsole.calledOnce).to.be.true;
    });

    it('should log "The total is: 20" when called with 10 and 10', function() {
        sendPaymentRequestToApi(10, 10);
        expect(spyConsole.calledWith('The total is: 20')).to.be.true;
        expect(spyConsole.calledOnce).to.be.true;
    });
});
