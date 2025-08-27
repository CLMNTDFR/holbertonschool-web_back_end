const expect = require('chai').expect;
const { getPaymentTokenFromAPI } = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
    it('should return a resolved promise with a success message when success is true', function(done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                expect(response).to.deep.equal({data: 'Successful response from the API'});
                done();
            })
            .catch(error => {
                done(error);
            });
    });

    it('should return a rejected promise when success is false', function(done) {
        getPaymentTokenFromAPI(false)
            .then(response => {
                done(new Error('Expected method to reject.'));
            })
            .catch(error => {
                expect(error.message).to.equal('Failed response from the API');
                done();
            });
    });
});
