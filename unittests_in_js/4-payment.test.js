const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
    it('should call calculateNumber with "SUM", totalAmount, and totalShipping', function() {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const spyConsole = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);

        expect(stub.calledWith('SUM', 100, 20)).to.be.true;
        expect(spyConsole.calledWith('The total is: 10')).to.be.true;

        stub.restore();
        spyConsole.restore();
    });
});
