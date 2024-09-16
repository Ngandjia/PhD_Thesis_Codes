R=QQ[s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, x, y, Degrees=>{0,0,0,0,0,0,0,0,1,1}, MonomialOrder => GRevLex];

j2 = s_4*s_5 - 3*s_3*s_6 + 3*s_2*s_7 - s_1*s_8;
j41 = 3*s_2^2*s_3^2 - 4*s_1*s_3^3 - 4*s_2^3*s_4 + 6*s_1*s_2*s_3*s_4 - s_1^2*s_4^2;
j42 = 3*s_6^2*s_7^2 - 4*s_5*s_7^3 - 4*s_6^3*s_8 + 6*s_5*s_6*s_7*s_8 - s_5^2*s_8^2;
j43 = 2*s_3^2*s_6^2 - 2*s_2*s_4*s_6^2 - 2*s_3^2*s_5*s_7 + 2*s_2*s_4*s_5*s_7 - s_2*s_3*s_6*s_7 + s_1*s_4*s_6*s_7 + 2*s_2^2*s_7^2 - 2*s_1*s_3*s_7^2 + s_2*s_3*s_5*s_8 - s_1*s_4*s_5*s_8 - 2*s_2^2*s_6*s_8 + 2*s_1*s_3*s_6*s_8;
j44 = -2*s_3^3*s_5 + 3*s_2*s_3*s_4*s_5 - s_1*s_4^2*s_5 + 3*s_2*s_3^2*s_6 - 6*s_2^2*s_4*s_6 + 3*s_1*s_3*s_4*s_6 + 3*s_2^2*s_3*s_7 - 6*s_1*s_3^2*s_7 + 3*s_1*s_2*s_4*s_7 - 2*s_2^3*s_8 + 3*s_1*s_2*s_3*s_8 - s_1^2*s_4*s_8;
j45 = -2*s_4*s_6^3 + 3*s_4*s_5*s_6*s_7 + 3*s_3*s_6^2*s_7 - 6*s_3*s_5*s_7^2 + 3*s_2*s_6*s_7^2 - 2*s_1*s_7^3 - s_4*s_5^2*s_8 + 3*s_3*s_5*s_6*s_8 - 6*s_2*s_6^2*s_8 + 3*s_2*s_5*s_7*s_8 + 3*s_1*s_6*s_7*s_8 - s_1*s_5*s_8^2;
j6 = -s_3^2*s_4*s_5*s_6^2 + s_2*s_4^2*s_5*s_6^2 + s_3^3*s_6^3 - s_1*s_4^2*s_6^3 + s_3^2*s_4*s_5^2*s_7 - s_2*s_4^2*s_5^2*s_7 - s_2*s_3*s_4*s_5*s_6*s_7 + s_1*s_4^2*s_5*s_6*s_7 - 3*s_2*s_3^2*s_6^2*s_7 + 3*s_1*s_3*s_4*s_6^2*s_7 + 2*s_2^2*s_4*s_5*s_7^2 - 2*s_1*s_3*s_4*s_5*s_7^2 + 3*s_2^2*s_3*s_6*s_7^2 - 3*s_1*s_2*s_4*s_6*s_7^2 - s_2^3*s_7^3 + s_1^2*s_4*s_7^3 - s_3^3*s_5^2*s_8 + s_2*s_3*s_4*s_5^2*s_8 + 3*s_2*s_3^2*s_5*s_6*s_8 - 2*s_2^2*s_4*s_5*s_6*s_8 - s_1*s_3*s_4*s_5*s_6*s_8 - 2*s_1*s_3^2*s_6^2*s_8 + 2*s_1*s_2*s_4*s_6^2*s_8 - 3*s_2^2*s_3*s_5*s_7*s_8 + 2*s_1*s_3^2*s_5*s_7*s_8 + s_1*s_2*s_4*s_5*s_7*s_8 + s_1*s_2*s_3*s_6*s_7*s_8 - s_1^2*s_4*s_6*s_7*s_8 + s_1*s_2^2*s_7^2*s_8 - s_1^2*s_3*s_7^2*s_8 + s_2^3*s_5*s_8^2 - s_1*s_2*s_3*s_5*s_8^2 - s_1*s_2^2*s_6*s_8^2 + s_1^2*s_3*s_6*s_8^2;

f1 = s_2^2*s_3^2 - 4/3*s_1*s_3^3 - 4/3*s_2^3*s_4 + 2*s_1*s_2*s_3*s_4 - 1/3*s_1^2*s_4^2;
f2 = s_6^2*s_7^2 - 4/3*s_5*s_7^3 - 4/3*s_6^3*s_8 + 2*s_5*s_6*s_7*s_8 - 1/3*s_5^2*s_8^2;
f3 = -120*s_2^2*s_5 + 240*s_1*s_2*s_6 - 120*s_1^2*s_7;
f4 = -96*s_2*s_3*s_5 + 72*s_2^2*s_6 + 96*s_1*s_3*s_6 - 48*s_1*s_2*s_7 - 24*s_1^2*s_8;
f5 = -48*s_3^2*s_5 - 24*s_2*s_4*s_5 + 72*s_2*s_3*s_6 + 24*s_1*s_4*s_6 + 24*s_1*s_3*s_7 - 48*s_1*s_2*s_8;
f6 = -48*s_3*s_4*s_5 + 24*s_2*s_4*s_6 + 72*s_2*s_3*s_7 + 24*s_1*s_4*s_7 - 48*s_2^2*s_8 - 24*s_1*s_3*s_8;
f7 = -24*s_4^2*s_5 - 48*s_3*s_4*s_6 + 72*s_3^2*s_7 + 96*s_2*s_4*s_7 - 96*s_2*s_3*s_8;
f8 = -120*s_4^2*s_6 + 240*s_3*s_4*s_7 - 120*s_3^2*s_8;
f9 = 120*s_3*s_5^2 - 240*s_2*s_5*s_6 + 120*s_1*s_6^2;
f10 = 24*s_4*s_5^2 + 48*s_3*s_5*s_6 - 72*s_2*s_6^2 - 96*s_2*s_5*s_7 + 96*s_1*s_6*s_7;
f11 = 48*s_4*s_5*s_6 - 24*s_3*s_5*s_7 - 72*s_2*s_6*s_7 + 48*s_1*s_7^2 - 24*s_2*s_5*s_8 + 24*s_1*s_6*s_8;
f12 = 48*s_4*s_6^2 + 24*s_4*s_5*s_7 - 72*s_3*s_6*s_7 - 24*s_3*s_5*s_8 - 24*s_2*s_6*s_8 + 48*s_1*s_7*s_8;
f13 = 96*s_4*s_6*s_7 - 72*s_3*s_7^2 - 96*s_3*s_6*s_8 + 48*s_2*s_7*s_8 + 24*s_1*s_8^2;
f14 = 120*s_4*s_7^2 - 240*s_3*s_7*s_8 + 120*s_2*s_8^2;
f15 = -6*s_2*s_3*s_5 + 6*s_1*s_4*s_5 + 12*s_2^2*s_6 - 12*s_1*s_3*s_6;
f16 = -4*s_3^2*s_5 + 4*s_2*s_4*s_5 - 2*s_2*s_3*s_6 + 2*s_1*s_4*s_6 + 8*s_2^2*s_7 - 8*s_1*s_3*s_7;
f17 = -8*s_3^2*s_6 + 8*s_2*s_4*s_6 + 2*s_2*s_3*s_7 - 2*s_1*s_4*s_7 + 4*s_2^2*s_8 - 4*s_1*s_3*s_8;
f18 = -12*s_3^2*s_7 + 12*s_2*s_4*s_7 + 6*s_2*s_3*s_8 - 6*s_1*s_4*s_8;
f19 = 12*s_2*s_6^2 - 12*s_2*s_5*s_7 - 6*s_1*s_6*s_7 + 6*s_1*s_5*s_8;
f20 = 8*s_3*s_6^2 - 8*s_3*s_5*s_7 - 2*s_2*s_6*s_7 - 4*s_1*s_7^2 + 2*s_2*s_5*s_8 + 4*s_1*s_6*s_8;
f21 = 4*s_4*s_6^2 - 4*s_4*s_5*s_7 + 2*s_3*s_6*s_7 - 8*s_2*s_7^2 - 2*s_3*s_5*s_8 + 8*s_2*s_6*s_8;
f22 = 6*s_4*s_6*s_7 - 12*s_3*s_7^2 - 6*s_4*s_5*s_8 + 12*s_3*s_6*s_8;
f23 = s_4*s_5 - 3*s_3*s_6 + 3*s_2*s_7 - s_1*s_8;

A=QQ[a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4, MonomialOrder => GRevLex];
projectionMap = map(A, R, {a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4, 0, 0});

j2 = projectionMap(j2);
j41 = projectionMap(j41);
j42 = projectionMap(j42);
j43 = projectionMap(j43);
j44 = projectionMap(j44);
j45 = projectionMap(j45);
j6 = projectionMap(j6);

f1 = projectionMap(f1);
f2 = projectionMap(f2);
f3 = projectionMap(f3);
f4 = projectionMap(f4);
f5 = projectionMap(f5);
f6 = projectionMap(f6);
f7 = projectionMap(f7);
f8 = projectionMap(f8);
f9 = projectionMap(f9);
f10 = projectionMap(f10);
f11 = projectionMap(f11);
f12 = projectionMap(f12);
f13 = projectionMap(f13);
f14 = projectionMap(f14);
f15 = projectionMap(f15);
f16 = projectionMap(f16);
f17 = projectionMap(f17);
f18 = projectionMap(f18);
f19 = projectionMap(f19);
f20 = projectionMap(f20);
f21 = projectionMap(f21);
f22 = projectionMap(f22);
f23 = projectionMap(f23);

J = ideal(j2, j41, j42, j43, j44, j45, j6);
ILimit = ideal(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23);

r = res ILimit;
phi0 = r.dd_1; -- is a 1 x 38 matrice
phi1 = r.dd_2; -- is a 38 x 132 matrice

phi0List = flatten entries phi0;
phi1List = flatten entries phi1;

nonzero0 = 0;
total0 = 0;
dict0 = new MutableHashTable
for element in phi0List do (
    total0 += 1;
    if element != 0 then (
        nonzero0 += 1;
        if member("degree " | toString((degree(element))_0), keys dict0) then (
            dict0#("degree " | toString((degree(element))_0)) += 1
        )
        else (
            dict0#("degree " | toString((degree(element))_0)) = 1
        );
    );
);
--for key in keys dict0 do (
    --print(toString key | " : " | toString dict0#key )
--);

nonzero1 = 0
total1 = 0
dict1 = new MutableHashTable
for element in phi1List do (
    total1 += 1;
    if element != 0 then (
        nonzero1 += 1;
        if member("degree " | toString((degree(element))_0), keys dict1) then (
            dict1#("degree " | toString((degree(element))_0)) += 1
        )
        else (
            dict1#("degree " | toString((degree(element))_0)) = 1
        );
    );
);
--for key in keys dict1 do (
    --print(toString key | " : " | toString dict1#key )
--);

label = 0
count = 0
for element in phi1List do (
    label += 1;
    if element != 0 then (
        if X(element) == 0 then (
        count += 1;
        --print("element " | toString(label) | " of degree " | toString((degree(element))_0))
        );
    )
    else (
        count += 1;
    );
);

standardBasisVector = (n, i) -> (
    v = new MutableList from for j from 0 to n-1 list 0*j4;
    v#i = 1;
    v = toList v;
    vector v
);