#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  list.forEach(element => {
    revList.unshift(element);
  });
  return revList;
};
