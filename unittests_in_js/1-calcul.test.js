const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('Test the calculateNumber sum, subtract and divide', function() {
    it('should return the sum of rounded a and b', function() {
        assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return the subtract of rounded a and b', function() {
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return the divide of rounded a and b', function() {
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return the divide by 0 error', function() {
        assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
});
