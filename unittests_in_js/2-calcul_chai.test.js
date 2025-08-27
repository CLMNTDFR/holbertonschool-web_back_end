const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('Test the calculateNumber sum, subtract and divide', function() {
    it('should return the sum of rounded a and b', function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return the subtract of rounded a and b', function() {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return the divide of rounded a and b', function() {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return the divide by 0 error', function() {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
