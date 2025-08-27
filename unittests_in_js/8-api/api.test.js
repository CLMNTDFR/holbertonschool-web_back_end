const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('should return correct status code and result', (done) => {
    request('http://localhost:7865', (err, res, text) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(text).to.equal('Welcome to the payment system');
      done();
    });
  });
});
