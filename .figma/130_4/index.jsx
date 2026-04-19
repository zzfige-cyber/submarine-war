import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <div className={styles.bg}>
        <div className={styles.group14}>
          <div className={styles.rectangle8}>
            <p className={styles.text3}>
              <span className={styles.text}>剩余技能点：</span>
              <span className={styles.text2}>5/5</span>
            </p>
          </div>
          <div className={styles.rectangle7}>
            <div className={styles.autoWrapper4}>
              <div className={styles.autoWrapper}>
                <p className={styles.text4}>移动速度</p>
                <p className={styles.text5}>为你的战舰提供更快的移动速度</p>
              </div>
              <div className={styles.autoWrapper2}>
                <p className={styles.text4}>装甲厚度</p>
                <p className={styles.text5}>为你的战舰提供更快的移动速度</p>
              </div>
              <div className={styles.autoWrapper3}>
                <p className={styles.text6}>弹药库</p>
                <p className={styles.text7}>为你的战舰提供更快的移动速度</p>
              </div>
            </div>
            <div className={styles.autoWrapper5}>
              <img src="../image/mo1o3b30-8ibzsaw.svg" className={styles.group6} />
              <img src="../image/mo1o3b30-8ibzsaw.svg" className={styles.group10} />
              <img src="../image/mo1o3b30-8ibzsaw.svg" className={styles.group10} />
            </div>
            <div className={styles.autoWrapper6}>
              <div className={styles.group2}>
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
              </div>
              <div className={styles.group8}>
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
              </div>
              <div className={styles.group8}>
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
                <div className={styles.ellipse4} />
              </div>
            </div>
            <div className={styles.autoWrapper7}>
              <img src="../image/mo1o3b30-9sjrxur.svg" className={styles.group6} />
              <img src="../image/mo1o3b30-9sjrxur.svg" className={styles.group10} />
              <img src="../image/mo1o3b30-9sjrxur.svg" className={styles.group10} />
            </div>
          </div>
        </div>
        <div className={styles.frame1}>
          <p className={styles.text8}>启航</p>
        </div>
      </div>
      <img
        src="../image/mo1o3b32-y0yl340.png"
        className={styles.jimeng2026041481561}
      />
      <div className={styles.rectangle14} />
      <p className={styles.text9}>潜艇大作战</p>
    </div>
  );
}

export default Component;
