const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Test the calculateNumber sum', function() {
    it('should return the sum of rounded a and b', function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
        assert.strictEqual(calculateNumber(-1.6, 3.6), 2);
        assert.strictEqual(calculateNumber(-4.6, 3), -2);
        assert.strictEqual(calculateNumber(-1.6, -3.2), -5);
    });
});