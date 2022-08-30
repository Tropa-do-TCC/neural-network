function [Evalues, Evectors, x_mean]=PCA(x)
<<<<<<< HEAD
disp('PCA')
disp(x)
=======
disp("PCA")
disp(x)
disp(size(x))
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7

s=size(x,2);
% Calculate the mean
x_mean=sum(x,2)/s;
<<<<<<< HEAD
disp('X_MEAN')
disp(x_mean)
disp('size')
=======
disp("X_MEAN")
disp(x_mean)
disp("size")
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7
disp(s)

% Substract the mean

matri=repmat(x_mean,1,s)
disp(matri)

first=(x-matri)
disp(first)

x2=first/ sqrt(s-1);
<<<<<<< HEAD
disp('x2')
=======
disp("x2")
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7
disp(x2)

% Do the SVD
[U2,S2,V] = svd(x2, 0);

disp("S2")
disp(S2)
disp("U2")
disp(U2)
Evalues=diag(S2).^2;
Evectors=bsxfun(@times,U2,sign(U2(1,:)));
<<<<<<< HEAD
disp('evalues e evectors criados')
=======
disp("evalues e evectors criados")
disp(Evalues)
disp(size(Evalues))
disp(Evectors)
disp(size(Evectors))
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7
