##Personal DEV notes

Notes and annotations from the reference c implenetation



### Polyseed Create 

Polyseed create function here:
https://github.com/tevador/polyseed/blob/b7c35bb3c6b91e481ecb04fc235eaff69c507fa1/src/polyseed.c#L57C17-L57C32


polyseed_status polyseed_create(unsigned features, polyseed_data** seed_out) {


the features are passed to 
make_features which takes the features passed to it and returns the bitmask least significant 3 bits (lsb) for it 
so 

Parameter features 



/* create seed */
    seed->birthday = birthday_encode(GET_TIME());
    seed->features = seed_features;
    memset(seed->secret, 0, sizeof(seed->secret));
    GET_RANDOM_BYTES(seed->secret, SECRET_SIZE);
    seed->secret[SECRET_SIZE - 1] &= CLEAR_MASK;

    /* encode polynomial */
    gf_poly poly = { 0 };
    polyseed_data_to_poly(seed, &poly);

    /* calculate checksum */
    gf_poly_encode(&poly);
    seed->checksum = poly.coeff[0];

    MEMZERO_LOC(poly);

    *seed_out = seed;


    