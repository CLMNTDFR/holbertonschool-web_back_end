function getPaymentTokenFromAPI(success) {
    if (success) {
        return Promise.resolve({data: 'Successful response from the API'});
    } else {
        return Promise.reject(new Error('Failed response from the API'));
    }
}

module.exports = { getPaymentTokenFromAPI };
